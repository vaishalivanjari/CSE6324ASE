/*
 * @source: https://github.com/trailofbits/not-so-smart-contracts/blob/master/wrong_constructor_name/incorrect_constructor.sol
 * @author: Ben Perez
 * Modified by Gerhard Wagner
 */

pragma solidity 0.4.24;

contract Missing {
    address private owner;
    uint public value;

    constructor() public {
        owner = msg.sender;
        value = 0;
    }

    function setValue(uint number) public {
        require(msg.sender == owner, "Unauthorized");
        value = number;
    }

    function getValue() public view returns (uint) {
        return value;
    }

    function withdraw() public {
        require(msg.sender == owner, "Unauthorized");
        msg.sender.transfer(address(this).balance);
    }
}
