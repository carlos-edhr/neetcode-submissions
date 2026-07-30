class Solution:

    def encode(self, strs: List[str]) -> str:
        # Input: strs =  ["Hello","World"] ,  ["", ""], []
        if not strs : 
            print("Empty strs: ", strs)
            return ""
        for idx, string in enumerate(strs):
            strs[idx] = string +  "_//98752//_"
        print("First strs transformation: ", strs)
        
        encoded_string = ""
        for word in strs:
            encoded_string += word
        
        print("second strs transformation: ", encoded_string)
        #Output: strs = "Hello World"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        # Input: s = "Hello World"
        if s == "":
            s = []
            return s
        decoded_list = s.split("_//98752//_")
        decoded_list.pop()

        print("third strs transformation: ", decoded_list)

        if not decoded_list:
            decoded_list.append("")
            return decoded_list



        # Output: strs =  ["Hello","World"]
        return decoded_list
