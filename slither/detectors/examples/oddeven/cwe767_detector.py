from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.core.solidity_types.elementary_type import ElementaryType
import re
from Crypto.Cipher import AES

class CWE767detector(AbstractDetector):
    ARGUMENT = "CWE767Detector"  # slither will launch the detector with slither.py --mydetector
    HELP = "CWE767:Critical private access in public method"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH
    WIKI = "https://cwe.mitre.org/data/definitions/767.html"
    WIKI_TITLE = "CWE767 Vulnerability example"
    WIKI_DESCRIPTION = "Detector example"
    WIKI_EXPLOIT_SCENARIO = "Adding a detector to find unencrypted private data on-chain is the main goal of the project plan. Often held misconception: Private data variables cannot be read. Although the contract is not disclosed, attackers can learn about its status by looking at contract transactions."
    WIKI_RECOMMENDATION = "To store private data on-chain or off-chain, it must be encrypted. Alternatively, private data can be modified in pure private function and that private function can be called in public function."

    def _detect(self):
        results = []
        encryption_regex = re.compile(r'AES|RSA|DES|3DES|Blowfish|Twofish|MD5|sha256|sha3|bcrypt|scrypt|keccak256|ripemd160|ecrecover|secp256k1')
        for contract in self.slither.contracts:
            for function in contract.functions:
                for node in function.nodes:
                    for variable in node.state_variables_written:
                        if(variable.visibility == "private"):
                            #check if data encryption is used
                            if(encryption_regex.search(node.expression.__str__()) and node.expression.__str__()):
                                break
                            else:
                                if function.visibility == "public" and variable.visibility == "private":
                                    info = ["CWE-767:Access to Critical Private Variable in public method in ", function,
                                        "\n", "\t-", "Illegal modification:", "\n", "\t-", node.expression.__str__(),
                                        "(", node.source_mapping.__str__(), ")\n"]
                                    res = self.generate_result(info)
                                    results.append(res)
        return results


