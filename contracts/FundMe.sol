// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract FundMe {
    using SafeMathChainlink for uint256;

    mapping(address => uint256) public addressToAmountFunded;
    address [] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeedContractAddress) public {
        priceFeed = AggregatorV3Interface(_priceFeedContractAddress);
        owner = msg.sender;
    }

    modifier onlyOwner {
        // Only the `owner` can call/transact this function
        require(msg.sender == owner);
        _;
    }

    function fund() public payable {
        // TODO: Write doc 

        uint256 minimumUsd = 50 * 10**18;
        require(
            getConversionRate(msg.value) >= minimumUsd,
            "More ETH required!"
        );
        addressToAmountFunded[msg.sender] = msg.value;
        funders.push(msg.sender);
    }

    function withdraw() public payable onlyOwner {

        msg.sender.transfer(address(this).balance);

        for(
            uint256 index = 0;
            index < funders.length;
            index++
        ) {
            address funder = funders[index];
            addressToAmountFunded[funder] = 0;
        }
    }
    function getPrice() public view returns (uint256) {
        // Returns the current `ETH/USD` price in `wei`

        (, int256 answer, , , ) = priceFeed.latestRoundData();
        // `answer` is in `gwei`

        return uint256(answer * 10000000000);
    }
    
    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        // Returns the amount in USD for `ethAmount`
        
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;

        return ethAmountInUsd;
    }

    function getEntranceFee() public view returns (uint256) {
        // Returns the minimum amount in Eth needed to be eligible to Fund
        // Returns in wei
        

        uint256 minimumUsd = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;

        return (minimumUsd * precision) / price;
    }
}