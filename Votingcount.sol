pragma solidity ^0.4.0;

contract Votingcount
{
     mapping(address => int) public voter ;
     uint[6] public vote = [0,0,0,0,0,0] ;
     
     
     function setaddress(int i) public 
     {
         address ad = msg.sender;
         voter[ad] = i;
          uint temp = uint(i);
          vote[temp]++;
     }
   
      function getarray(uint _index) view public returns(uint){
         return vote[_index];
      }
    
}