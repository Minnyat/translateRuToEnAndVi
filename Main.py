from config import nameFileIn,nameFileOut
import function
def main():
    data = function.readFile(nameFileIn)
    dataout = function.change(data)
    function.Writefile(nameFileOut,dataout)
main()