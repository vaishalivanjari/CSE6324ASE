/*
 * @source: https://gist.github.com/manojpramesh/336882804402bee8d6b99bea453caadd#file-odd-even-sol
 * @author: https://github.com/manojpramesh
 * Modified by Kaden Zipfel
 */
pragma solidity 0.5.0;

contract OddEven {
    struct Player {
        bytes32 encryptedAddr;
        bytes32 encryptedNumber;
    }

    Player[2] private players;
    uint count = 0;
    bytes32 private key;
    address internal owner;

    constructor() public{
        owner = msg.sender;
    }

    function play(bytes32 number) public payable {
        require(msg.value == 1 ether, 'msg.value must be 1 eth');
        players[count] = Player(keccak256(abi.encodePacked(msg.sender)), keccak256(abi.encodePacked(number)));
        count++;
        if (count == 2) selectWinner();
    }

    function selectWinner() private {
        require(msg.sender == owner, 'unauthorized');
        msg.sender.transfer(address(this).balance);
        delete players;
        count = 0;
    }

    function setKey(bytes32 _key) public {
        key = keccak256(abi.encodePacked(_key));
    }

    function decryptPlayer(uint index) public view returns (address, uint) {
        bytes32 addr = players[index].encryptedAddr;
        bytes32 number = players[index].encryptedNumber;
        require(keccak256(abi.encodePacked(msg.sender, key)) == addr, 'unauthorized');
        return (address(bytes20(addr)), uint(number));
    }
}
