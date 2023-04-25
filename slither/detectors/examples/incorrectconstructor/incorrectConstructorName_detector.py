from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.formatters.naming_convention.naming_convention import custom_format
from difflib import SequenceMatcher

class IncorrectConstructorName(AbstractDetector):
    """
    Documentation
    """

    ARGUMENT = 'IncorrectConstructorName' # slither will launch the detector with slither.py --detect mydetector
    HELP = 'CWE-665:Improper Initialization'
    IMPACT = DetectorClassification.INFORMATIONAL
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = 'https://cwe.mitre.org/data/definitions/665.html'

    WIKI_TITLE = 'Incorrect Constructor Name'
    WIKI_DESCRIPTION = 'Detector Example'
    WIKI_EXPLOIT_SCENARIO = 'The resource may not be initialized by the product or may be initialized incorrectly, exposing the resource in an unexpected state when requested or used.'
    WIKI_RECOMMENDATION = 'Avoid using older pragma versions & declare constructor using keyword constructor()'

    def _detect(self):
        results = []

        for contract in self.slither.contracts:
            for function in contract.functions:
                temp = SequenceMatcher(None, contract.name, function.name).ratio()
                #print(function.name,' ',temp)
                for variable in function.variables_written:
                    if(variable in contract.state_variables):
                        if (function.visibility == 'public' and function.return_type is None):
                            if(temp >= 0.50):
                                info = ["CWE-665:Improper Intialization of constructor in ", function, "\n", "\t-",
                                        "Improper initizalition of constructor", "(",
                                        function.source_mapping.__str__().split('#')[0], "#",
                                        function.source_mapping.lines[0].__str__(), ")", "\n"]
                                res = self.generate_result(info)
                                results.append(res)
        return results
