class Solution:

    def encode(self, strs: List[str]) -> str:
        # Input: strs =  ["Hello","World"] ,  ["", ""], []
        if not strs : 
            return ""
        for idx, string in enumerate(strs):
            strs[idx] = string +  "_//98752//_"
        
        encoded_string = ""
        for word in strs:
            encoded_string += word
        
        #Output: strs = "Hello World"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        # Input: s = "Hello World"
        if s == "":
            s = []
            return s
        decoded_list = s.split("_//98752//_")
        decoded_list.pop()


        if not decoded_list:
            decoded_list.append("")
            return decoded_list



        # Output: strs =  ["Hello","World"]
        return decoded_list
