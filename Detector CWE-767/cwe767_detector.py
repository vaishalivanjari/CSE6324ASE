from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.core.solidity_types.elementary_type import ElementaryType


class CWE767detector(AbstractDetector):
    ARGUMENT = "CWE767Detector"  # slither will launch the detector with slither.py --mydetector
    HELP = "Function named CWE767"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH
    WIKI = "https://cwe.mitre.org/data/definitions/767.html"
    WIKI_TITLE = "CWE767 example"
    WIKI_DESCRIPTION = "Detector example"
    WIKI_EXPLOIT_SCENARIO = ".."
    WIKI_RECOMMENDATION = ".."

    def _detect(self):
        results = []
        # for contract in self.slither.contracts:
        #     for function in contract.functions:
        #         for variable in contract.variables:
        #             print(function.name," ", function.visibility, " " ,variable, " ", variable.visibility)
        #             if variable.visibility == 'private' :
        #                 print(variable.name)
        # return results
        for contract in self.slither.contracts:
            for function in contract.functions:
                # for variable in function.variables:
                # for opr in function.variables_written:
                    # print("Opr ", "func:",function.name, " ",opr," ",opr.visibility, " ")
                for node in function.nodes:
                    for variable in node.state_variables_written:
                        if function.visibility == "public" and variable.visibility == "private":
                            info=["CWE-767:Access to Critical Private Variable in public method in ", function, "\n", "\t-","Illegal modification:","\n", "\t-", node.expression.__str__(),"(",node.source_mapping.__str__(),")\n"]
                            # info+= ["\tIllegal modification:\n", "\t", node.expression,"\n"]
                            res = self.generate_result(info)
                            results.append(res)
                    # if function.visibility == "public" and opr.visibility == "private":

                    # print(function.name," ", function.visibility, " " ,variable, " ", variable.visibility)
                    # if variable.visibility == 'private' :
                    #     print(variable.name)
        return results

