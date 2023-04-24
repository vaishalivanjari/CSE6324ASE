# Adding a new detector to Slither, A Static Analyzer Tool for Ethereum Blockchain

The plan is to extend the Slither analysis framework by adding two detectors. Slither is the open-source static analysis framework for Solidity that may be used to find holes in smart contracts. Red, yellow, and green are used by Slither to denote the impact and severity of vulnerabilities, correspondingly, for high, medium, low, and informational. The project consists of adding two detectors as follows:

i) Detector to detect unencrypted private data on-chain 

To detect vulnerability CWE-767:Critical private access in public method

Adding a detector to find unencrypted private data on-chain is the main goal of the project plan. In the final iteration, the detector to detect vulnerability CWE-767 is completed where the detector is checking if private is encrypted or not and is being modified in a public function. Often held misconception: Private data variables cannot be read. Although the contract is not disclosed, attackers can learn about its status by looking at contract transactions. To store private data on-chain or off-chain, it must be encrypted. Alternatively, private data can be modified in pure private function and that private function can be called in public function.


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
    
