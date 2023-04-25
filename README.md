# Adding a new detector to Slither, A Static Analyzer Tool for Ethereum Blockchain

The plan is to extend the Slither analysis framework by adding two detectors. Slither is the open-source static analysis framework for Solidity that may be used to find holes in smart contracts. Red, yellow, and green are used by Slither to denote the impact and severity of vulnerabilities, correspondingly, for high, medium, low, and informational. The project consists of adding two detectors as follows:

i) Detector to detect unencrypted private data on-chain ii)	Detector to detect incorrect constructor name 

The main goal of the project plan is to propose results after adding the above two detectors. Contrary to general opinion, private data variables can be read. Attackers can discover the status of the contract by examining contract transactions even when the contract is not made public. It must be encrypted to be stored privately, either on-chain or off-chain[3]. As an alternative, private data can be altered in a pure private function and called from a public function. These mitigations are tested in the proposed detector for CWE-767. The point to be noted is that Slither does not detect this vulnerability before adding the CWE-767 detector.
In the final iteration, the detector to detect vulnerability CWE-767 is completed where the detector is checking if private data is encrypted or not and if it is being modified in a public function. The project checks every assignment to private data and validates if it is encrypted or not. If data is encrypted, then it can be modified in a public function. Data encryption is checked using regular expressions. As Slither has very few inbuilt cryptographic functions[13], the regEx expression uses external cryptographic functions as well. To check if private data is being modified or not in a public function, the project proposed the solution of checking the visibility of the function and if it is public then accessing all the state variables written in that public function. The point to note is local variables cannot be private in solidity language.  
The idea of adding another detector to find incorrect constructor names[11] was proposed in the previous iteration. Constructors are unique functions that are only used once when creating contracts. They frequently carry out crucial, exclusive tasks including identifying the contract's owner. The only way to define a constructor in Solidity before version 0.4.24 was to write a function with the same name as the contract class that contained it. If a function's name differs slightly from the contract name, it becomes a regular, callable function and is no longer intended to serve as a constructor. When smart contract code is utilized under a new name without changing the name of the constructor function, this practice might occasionally cause security problems.
In the final iteration, the detector to detect incorrect constructor names related to CWE-665 is completed where the detector differentiates in a regular callback function and constructor using the special characteristics of the constructor such as the constructor is used to initialize state variables, the visibility of the constructor should be public, and constructor does not have a return type. The project also proposed for similarity matrix to check the similarity[14] between the constructor declared using the function and contract name and set the threshold above 0.5. The proposed solution faced issues when there is a setter function that does not have any return type, visibility is public which are almost similar characteristics as the constructor and used to assign values to state variables, and the contract has an incorrect/previous constructor name that does not meet the threshold value 0.5 for the similarity between the contract name and the constructor’s name.

## Installation
## 
> Tools required

##
| SOFTWARE | TOOLS |
| -------- | ------ |
| Solidity compiler | [solc-0.5.0](https://docs.soliditylang.org/en/v0.8.17/installing-solidity.html) |
| Solidity complier version manager | [solc-select-1.0.2](https://github.com/crytic/solc-select) |
| Slither analyzer | [slither-analyzer-0.9.3](https://github.com/crytic/slither) |

- Add detector to all_detectors.py file, add the intended detector from the detectors folder
- Use the input file from the detector folder and place it in project directory
- Run the analyzer with the following command: 
    sh
    slither <input_contract_file.sol>
- To change the version of solc compiler using solc-select, run the following command:
    solc-select install <version>
    solc-select use <version>
-Proposed detector files can be found in CSE6324ASE/slither/detectors/examples/
    


    
