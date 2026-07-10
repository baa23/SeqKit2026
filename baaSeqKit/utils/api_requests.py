import requests
import xmltodict
import logging
from baaSeqKit.logger import setup_logging

logger = logging.getLogger(__name__)


class TranscriptIdError(Exception):
    """
    Raised when a transcript identifier is invalid.
    """
    pass

# ------------------------------------------------------------------
# Python classes and objects
#
# A class is a blueprint for creating objects. An object groups together
# related data (attributes) and functions (methods) into a single unit.
#
# In this example we create a SequenceAPI object because all of the
# functionality relates to interacting with biological sequence
# databases. The object stores information shared by every request,
# such as the HTTP session, timeout value and API URLs, while its
# methods perform specific tasks such as retrieving transcripts from
# GenBank or Ensembl.
#
# Organising the code this way keeps related functionality together,
# reduces duplication and makes it easy to add support for additional
# APIs in the future.
# ------------------------------------------------------------------
class SequenceAPI:
    """
    Interface to external sequence databases.

    Current support
    ---------------
    - GenBank / RefSeq
    - Ensembl (planned)
    - HGNC (planned)
    - UniProt (planned)
    - ClinVar (planned)
    """

    def __init__(self, timeout=30):
        """
        Initialise the API interface.
        """

        # Session configuration
        self.timeout = timeout

        # Create a persistent HTTP session.
        # Unlike requests.get(), a Session reuses TCP connections across multiple
        # requests (connection pooling), making repeated API calls more efficient.
        # It also provides a central place to configure headers, authentication,
        # cookies and retry behaviour if required in the future.
        self.session = requests.Session()

        # API endpoints.
        #
        # These URLs identify the web services used by SeqToolkit to retrieve
        # biological data.
        #
        # The leading underscore (_) is a Python naming convention indicating
        # that these attributes are intended for internal use within the class.
        # Unlike some programming languages, Python does not enforce private
        # variables. Instead, it relies on naming conventions:
        #
        #     public_attribute      Intended for anyone to use.
        #     _internal_attribute   Intended for use inside the class only
        #                           (a convention, not enforced).
        #     __private_attribute   Name-mangled by Python to make accidental
        #                           access more difficult.
        #
        # The public methods of this class (e.g. fetch_genbank_transcript())
        # use these endpoint URLs internally when communicating with each
        # external database.

        self._genbank_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
        self._ensembl_url = "https://rest.ensembl.org"
        self._ensembl_37_url = "https://grch37.rest.ensembl.org"
        self._hgnc_url = "https://rest.genenames.org"
        self._uniprot_url = "https://rest.uniprot.org"
        self._clinvar_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

        logger.debug("Instance of SequenceAPI initialised")
    # ------------------------------------------------------------------
    # Internal HTTP methods
    # ------------------------------------------------------------------

    def _get(self, base_url, endpoint="", params=None, headers=None):
        """
        Generic HTTP GET helper.
        """

        url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        try:
            response = self.session.get(
                url,
                params=params,
                headers=headers,
                timeout=self.timeout,
            )
            # logger.debug(f"response text {response.text}")
            response.raise_for_status()

            return response

        except requests.exceptions.RequestException:
            logger.exception(f"Failed GET request: {url}")
            raise

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # @staticmethod tells Python that this method does not need access
    # to the object itself (self).
    #
    # Normally, methods inside a class receive the current object as their
    # first argument:
    #
    #     def my_method(self):
    #
    # However, this validation function only examines the transcript ID
    # passed to it. It doesn't read or modify any attributes of the
    # SequenceAPI object.
    #
    # Using @staticmethod tells Python that this function behaves like a
    # regular function, but we keep it inside the class because it is
    # closely related to the SequenceAPI.
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_refseq_transcript(transcript_id):
        """
        Validate a RefSeq transcript accession.
        """

        if not transcript_id.startswith(("NM_", "NR_")):
            raise TranscriptIdError(
                f"{transcript_id} is not a supported RefSeq transcript."
            )

        if "." not in transcript_id:
            raise TranscriptIdError(
                f"{transcript_id} must include a version number."
            )
        logger.debug("RefSeq transcript valid")

    @staticmethod
    def _validate_ensembl_transcript(transcript_id):
        """
        Validate a RefSeq transcript accession.
        """

        if not transcript_id.startswith(("ENST")):
            raise TranscriptIdError(
                f"{transcript_id} is not a supported Ensembl transcript."
            )

        #  if "." not in transcript_id:
        #      raise TranscriptIdError(
        #          f"{transcript_id} must include a version number."
        #     )
        
        logger.debug("Ensembl transcript valid")

    # ------------------------------------------------------------------
    # GenBank
    # ------------------------------------------------------------------

    def fetch_genbank_transcript(self, transcript_id):
        """
        Fetch a RefSeq transcript from GenBank.
        """

        self._validate_refseq_transcript(transcript_id)

        response = self._get(
            self._genbank_url,
            "efetch.fcgi",
            params={
                "db": "nucleotide",
                "id": transcript_id,
                "retmode": "xml",
            },
        )

        return xmltodict.parse(response.text)["GBSet"]["GBSeq"]

    # ------------------------------------------------------------------
    # Ensembl
    # ------------------------------------------------------------------

    def fetch_ensembl_transcript(self, transcript_id):
        """
        Fetch Ensembl transcript information.

        """

        self._validate_ensembl_transcript(transcript_id)

        response = self._get(
            self._ensembl_url,
            ("/lookup/id/" + transcript_id), 
            headers={"Accept": "application/json"}
        )

        return response.json()

    # ------------------------------------------------------------------
    # HGNC
    # ------------------------------------------------------------------

    def fetch_hgnc_gene(self, gene_symbol):
        """
        Fetch HGNC gene information.

        Placeholder.
        """

        raise NotImplementedError()

    # ------------------------------------------------------------------
    # UniProt
    # ------------------------------------------------------------------

    def fetch_uniprot_protein(self, accession):
        """
        Fetch a UniProt protein.

        Placeholder.
        """

        raise NotImplementedError()

    # ------------------------------------------------------------------
    # ClinVar
    # ------------------------------------------------------------------

    def fetch_clinvar_record(self, accession):
        """
        Fetch a ClinVar record.

        Placeholder.
        """

        raise NotImplementedError()


if __name__ == "__main__":

    # Initialise logging
    setup_logging()
    logger.info("Program started")

    api = SequenceAPI()

    record_refseq = api.fetch_genbank_transcript("NM_000093.5")
    logger.debug("RefSeq API responded")
    
    print(f"Accession: {record_refseq["GBSeq_accession-version"]}")
    print(f"Name: {record_refseq["GBSeq_definition"]}")
    print(f"KeyWords: {record_refseq["GBSeq_keywords"]}")

    print(f"Sequence: {record_refseq["GBSeq_sequence"].upper()}")

    for feature in record_refseq["GBSeq_feature-table"]["GBFeature"]:

        if feature["GBFeature_key"] == "gene":
            print(f"GeneSymbol: {feature["GBFeature_quals"]["GBQualifier"][0]["GBQualifier_value"]}")

        elif feature["GBFeature_key"] == "CDS":
            print(f"CDS_Start: {feature["GBFeature_intervals"]["GBInterval"]["GBInterval_from"]}")
            print(f"CDS_End: {feature["GBFeature_intervals"]["GBInterval"]["GBInterval_to"]}")
    
    print("---------------------------------------------------------------------")
    
    record_ensembl = api.fetch_ensembl_transcript("ENST00000371817")
    logger.debug("Ensembl API responded")
    
    print(f"Ensembl API - {record_ensembl["display_name"]}")

    logger.info("Program completed")