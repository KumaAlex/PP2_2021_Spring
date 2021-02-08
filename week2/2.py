class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        global x
        x = command.replace("()","o")
        x = x.replace("(al)","al")
        return x