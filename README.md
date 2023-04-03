The plan is to extend the Slither analysis framework by adding two detectors. Slither is the open-source static analysis framework for Solidity that may be used to find holes in smart contracts. Red, yellow, and green are used by Slither to denote the impact and severity of vulnerabilities, correspondingly, for high, medium, low, and informational. The project consists of adding two detectors as follows:

i) Detector to detect unencrypted private data on-chain ii) Detector to detect incorrect constructor name

To detect vulnerability CWE-767:Critical private access in public method

Adding a detector to find unencrypted private data on-chain is the main goal of the project plan. Often held misconception: Private data variables cannot be read. Although the contract is not disclosed, attackers can learn about its status by looking at contract transactions. To store private data on-chain or off-chain, it must be encrypted. Alternatively, private data can be modified in pure private function and that private function can be called in public function.

To detect the incorrect constructor name in solidity smart contracts

Adding another detector to find incorrect constructor name can make the smart contract exploitable to attacks. Constructors were formerly identified in Solidity v0.4.22 as functions with the same name as the contract they were contained in. If the contract name gets changed in development, then declaring constructor using function name will act as normal callable function. Especially if the constructor is conducting privileged activities, this could have disastrous results.

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
    