import unittest
from TestUtils import TestUtils

# lỗi
'''
- dư/thiếu arg
- khác tên hàm
- tên biến sai
- tên value sai
- ko begin
- ko end
- undeclare
- ko tìm thấy look

'''


class TestSymbolTable(unittest.TestCase):
    # args 0-> 6
    def test_0(self):
        input = ["INSERT a1 number string", "INSERT b2 string"]
        expected = ["Invalid: INSERT a1 number string"]

        self.assertTrue(TestUtils.check(input, expected, 100))

    def test_1(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x"]
        expected = ["Invalid: ASSIGN x"]

        self.assertTrue(TestUtils.check(input, expected, 101))

    def test_2(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y",
            "ASSIGN x 'abc'",
        ]
        expected = ["Invalid: ASSIGN y"]

        self.assertTrue(TestUtils.check(input, expected, 102))

    def test_3(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "BEGIN",
            "INSERT y string",
            "LOOKUP",
            "END",
            "END"
        ]
        expected = ["Invalid: LOOKUP"]

        self.assertTrue(TestUtils.check(input, expected, 103))

    def test_4(self):
        input = [
            ""
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 104))

    def test_5(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z",
            "PRINT",
            "END",
        ]
        expected = ["Invalid: INSERT z"]

        self.assertTrue(TestUtils.check(input, expected, 105))
    
    def test_6(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "z//1 x//1 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 106))

    def test_7(self):
        input=[
            "INSERT he@s number" 
        ]
        expected = ["Invalid: INSERT he@s number"]

        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_8(self):
        input=[
            "INSERT a number",
            "ASSIGN a 10.3"
        ]
        expected = ["Invalid: ASSIGN a 10.3"]

        self.assertTrue(TestUtils.check(input, expected, 146))

    def test_9(self):
        input=[
            "INSERT a number",
            "ASSIGN a '10'"
        ]
        expected = ["TypeMismatch: ASSIGN a '10'"]

        self.assertTrue(TestUtils.check(input, expected, 147))


    def test_10(self):
        input = [
            "INSERT x string",
            "INSERT y string",
            "INSERT z number"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 148))

    def test_11(self):
        input = [
            "INSERT x string",
            "INSERT y  string",
            "INSERT z number"
        ]
        expected = ["Invalid: INSERT y  string"]

        self.assertTrue(TestUtils.check(input, expected, 149))

    def test_12(self):
        input = [
            "INSERT x string",
            " INSERT y string",
            "INSERT   z number"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 150))

    def test_13(self):
        input = [
            "INSERT x_ number",
            "INSERT y4_3y string",
            "INSERT _z number"
        ]
        expected = ["Invalid: INSERT _z number"]

        self.assertTrue(TestUtils.check(input, expected, 151))

    def test_14(self):
        input = [
            "INSERT x string",
            "BEGIN",
            "INSERT x number",
            "END",
            "INSERT y number",
            "INSERT z string"
        ]
        expected = ["success","success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 152))

    def test_15(self):
        input = [
            "INSERT x string",
            "INSERT y string",
            "insert a number",
            "INSERT z number"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 153))

    def test_16(self):
        input = [
            "INSERT x string",
            "INSERT y string",
            "INSERT z number"
        ]
        expected = ["success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 154))

    def test_17(self):
        input = [
            "INSERT x string",
            "INSERT y string",
            "INSERT x number"
        ]
        expected = ["Redeclared: INSERT x number"]

        self.assertTrue(TestUtils.check(input, expected, 155))

    def test_18(self):
        input = [
            "INSERT x string",
            "INSERT y int",
            "INSERT z number string number"
        ]
        expected = ["Invalid: INSERT y int"]

        self.assertTrue(TestUtils.check(input, expected, 156))

    def test_19(self):
        input = [
            "INSERT x string",
            "INSERT y strIng",
            "INSERT z number"
        ]
        expected = ["Invalid: INSERT y strIng"]

        self.assertTrue(TestUtils.check(input, expected, 157))

    def test_20(self):
        input = [
            "INSERT x string",
            "INSERT y~3dx string",
            "INSERT z number"
        ]
        expected = ["Invalid: INSERT y~3dx string"]

        self.assertTrue(TestUtils.check(input, expected, 158))

    def test_21(self):
        input = [
            "INSERT x@- string",
            "INSERT y3dx string",
            "INSERT z number"
        ]
        expected = ["Invalid: INSERT x@- string"]

        self.assertTrue(TestUtils.check(input, expected, 159))

    def test_22(self):
        input = [
            "INSERT D2 string"
        ]
        expected = ["Invalid: INSERT D2 string"]

        self.assertTrue(TestUtils.check(input, expected, 160))

    def test_23(self):
        input = [
            "INSERT x string",
            "INSERT 2 number",
            "INSERT e_141gf number",
            "INSERT z number",
            "INSERT b string",
            "INSERT e_141gf string"
        ]
        expected = ["Invalid: INSERT 2 number"]

        self.assertTrue(TestUtils.check(input, expected, 161))

    def test_24(self):
        input = [
            "INSERT x string",
            "INSERT y___ string",
            "INSERT e string",
            "INSERT string string"
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 162))

#TEST ASSIGN

    def test_25(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 233",
            "ASSIGN y 'test'"
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 163))

    def test_26(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT z string",
            "ASSIGN y 'test'",
            "ASSIGN x '148'"
        ]
        expected = ["TypeMismatch: ASSIGN x '148'"]

        self.assertTrue(TestUtils.check(input, expected, 164))

    def test_27(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN y '213'",
            "ASSIGN y 'test'",
            "ASSIGN x 999"
        ]
        expected = ["success","success","success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 165))

    def test_28(self):
        input = [
            "INSERT a string",
            "INSERT b string",
            "ASSIGN b 'test'",
            "ASSIGN a '123'",
            "ASSIGN b a"
        ]
        expected = ["success","success","success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 166))

    def test_29(self):
        input = [
            "INSERT x number",
            "INSERT z string",
            "ASSIGN y 'un'",
            "ASSIGN x 0",
            "ASSIGN z 099"
        ]
        expected = ["Undeclared: ASSIGN y 'un'"]

        self.assertTrue(TestUtils.check(input, expected, 167))

    def test_30(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN y x"
        ]
        expected = ["TypeMismatch: ASSIGN y x"]

        self.assertTrue(TestUtils.check(input, expected, 168))

    def test_31(self):
        input = [
            "INSERT x number",
            "ASSIGN x y"
        ]
        expected = ["Undeclared: ASSIGN x y"]

        self.assertTrue(TestUtils.check(input, expected, 169))

    def test_32(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT z string",
            "ASSIGN y 'undeclared'",
            "ASSIGN z x"
        ]
        expected = ["TypeMismatch: ASSIGN z x"]

        self.assertTrue(TestUtils.check(input, expected, 170))

    def test_33(self):
        input = [
            "INSERT x number",
            "ASSIGN x 113.114",
        ]
        expected = ["Invalid: ASSIGN x 113.114"]

        self.assertTrue(TestUtils.check(input, expected, 171))

    def test_34(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT z string",
            "ASSIGN y 'RuN'",
            "ASSIGN x 666",
            "ASSIGN z 'teS_t'"
        ]
        expected = ["Invalid: ASSIGN z 'teS_t'"]

        self.assertTrue(TestUtils.check(input, expected, 172))

    def test_35(self):
        input = [
            "INSERT x string",
            "INSERT y number",
            "ASSIN x ''"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 173))

    def test_36(self):
        input = [
            "INSERT x string",
            "ASSIGN x 'hello"
        ]
        expected = ["Invalid: ASSIGN x 'hello"]

        self.assertTrue(TestUtils.check(input, expected, 174))

    def test_37(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT z string",
            "ASSIGN y 'test'",
            "ASSIGN x 123",
            "ASSIGN z '456'"
        ]
        expected = ["success","success","success","success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 175))


    def test_38(self):
        input = [
            "INSERT x string",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "INSERT y number",
            "BEGIN",
            "INSERT x number",
            "INSERT z string",
            "END",
            "END"
        ]
        expected = ["success", "success", "success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 176))

#TEST BEGIN/END

    def test_39(self):
        input = [
            "BEGIN"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 177))

    def test_40(self):
        input = [
            "BEGIN",
            "BEGIN"
        ]
        expected = ["UnclosedBlock: 2"]

        self.assertTrue(TestUtils.check(input, expected, 178))

    def test_41(self):
        input = [
            "END"
        ]
        expected = ["UnknownBlock"]

        self.assertTrue(TestUtils.check(input, expected, 179))

    def test_42(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x string",
            "INSERT z string",
            "END"
        ]
        expected = ["success","success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 180))

    def test_43(self):
        input = [
            "BEGIN",
            "INSERT a number",
            "END",
            "ASSIGN a 10"
        ]
        expected = ["Undeclared: ASSIGN a 10"]

        self.assertTrue(TestUtils.check(input, expected, 181))

    def test_44(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT z string",
            "END"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 182))

    def test_45(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "END",
            "INSERT x string",
        ]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 183))

    def test_46(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "BEGIN",
            "INSERT a number",
            "END",
            "BEGIN",
            "INSERT a number",
            "INSERT b string",
            "END",
        ]
        expected = ["success","success","success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 184))

#TEST LUKUP

    def test_47(self):
        input = [
            "LOOKUP B_"
        ]
        expected = ["Invalid: LOOKUP B_"]

        self.assertTrue(TestUtils.check(input, expected, 185))

    def test_48(self):
        input = [
            "LOOKUP find"
        ]
        expected = ["Undeclared: LOOKUP find"]

        self.assertTrue(TestUtils.check(input, expected, 186))

    def test_49(self):
        input = [
            "INSERT find number",
            "LOOKUP find"
        ]
        expected = ["success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 187))

    def test_50(self):
        input = [
            "INSERT a string",
            "INSERT x string",
            "ASSIGN x 'test'",
            "ASSIGN a x",
            "LOOKUP a x"
        ]
        expected = ["Invalid: LOOKUP a x"]

        self.assertTrue(TestUtils.check(input, expected, 188))

    def test_51(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "BEGIN",
            "INSERT c number",
            "ASSIGN c a",
            "INSERT y number",
            "LOOKUP y",
            "END",
            "LOOKUP b",
            "BEGIN",
            "INSERT x string",
            "INSERT y string",
            "LOOKUP y",
            "INSERT z string",
            "END"
        ]
        expected = ["success", "success", "success", "success", "success", "1", "0", "success", "success", "1", "success"]

        self.assertTrue(TestUtils.check(input, expected, 189))

    def test_52(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "LOOKUP x",
            "INSERT z string",
            "END",
            "END",
            "END"
        ]
        expected = ["success", "0","success"]

        self.assertTrue(TestUtils.check(input, expected, 190))

    def test_53(self):
        input = [
            "BEGIN",
            "INSERT z string",
            "END",
            "LOOKUP x"
        ]
        expected = ["Undeclared: LOOKUP x"]

        self.assertTrue(TestUtils.check(input, expected, 191))

    def test_54(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT f string",
            "INSERT a string",
            "LOOKUP a",
            "END",
            "ASSIGN a 10",
            "LOOKUP a"
        ]
        expected = ["success","success","success","1","success","0"]

        self.assertTrue(TestUtils.check(input, expected, 192))

    def test_55(self):
        input = [
            "INSERT y string",
            "BEGIN",
            "ASSIGN y 'run'",
            "INSERT y string",
            "END",
            "LOOKUP y"
        ]
        expected = ["success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 193))

    def test_56(self):
        input = [
            "INSERT a string",
            " ASSIGN a 'add'"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 194))

    def test_57(self):
        input = [
            "ASSIGN s 10"
        ]
        expected = ["Undeclared: ASSIGN s 10"]

        self.assertTrue(TestUtils.check(input, expected, 195))

    def test_58(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z string",
            "ASSIGN x 148",
            "PRINT",
            "END",
            "PRINT"
        ]
        expected = ["success", "success", "success", "success", "x//0 y//0 z//1", "x//0 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 196))

    def test_59(self):
        input = [
            "INSERT a string",
            "BEGIN",
            "INSERT b number",
            "INSERT c number",
            "PRINT",
            "END",
            "PRINT",
        ]
        expected = ["success", "success", "success", "a//0 b//1 c//1", "a//0"]

        self.assertTrue(TestUtils.check(input, expected, 197))

    def test_60(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "ASSIGN x y",
            "END"
        ]
        expected = ["TypeMismatch: ASSIGN x y"]

        self.assertTrue(TestUtils.check(input, expected, 198))

    def test_61(self):
        input = [
            "BEGIN",
            "INSERT a number",
            "INSERT b string",
            "END",
            "PRINT"
        ]
        expected = ["success", "success", ""]

        self.assertTrue(TestUtils.check(input, expected, 199))

    def test_62(self):
        input = [
            "PRINT",
            "INSERT a number",
            "INSERT b string"
        ]
        expected = ["", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 200))

    def test_63(self):
        input = [
            "Print"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 202))

    def test_65(self):
        input = [
            "RPRINT",
            "rprint"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 203))

    def test_66(self):
        input = [
            "RPRINT x"
        ]
        expected = ["Invalid: RPRINT x"]

        self.assertTrue(TestUtils.check(input, expected, 204))

    def test_67(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z string",
            "ASSIGN x 148",
            "RPRINT",
            "PRINT",
            "END",
            "RPRINT"
        ]
        expected = ["success", "success", "success", "success", "z//1 y//0 x//0","x//0 y//0 z//1", "y//0 x//0"]

        self.assertTrue(TestUtils.check(input, expected, 205))

    def test_68(self):
        input = [  
            "RPINT"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 206))

    def test_69(self):
        input = [
            "PRINT",
            "INSERT a string",
            "RPRINT",
            "PRINT",
        ]
        expected = ["", "success", "a//0","a//0"]

        self.assertTrue(TestUtils.check(input, expected, 207))

    def test_70(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "END",
            "RPRINT"
        ]
        expected = ["success", "success", ""]

        self.assertTrue(TestUtils.check(input, expected, 208))

    def test_71(self):
        input = [
            "PRINT",
            "BEGIN",
            "INSERT a string",
            "RPRINT",
            "END",
            "PRINT"
        ]
        expected = ["", "success", "a//1",""]

        self.assertTrue(TestUtils.check(input, expected, 209))

    def test_72(self):
        input = [
            "BEGIN",
            "PRINT",
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 210))

    def test_73(self):
        input = [
            "PRINT",
            "INSERT a string",
            "BEGIN",
            "RPRINT",
            "END",
        ]
        expected = ["", "success", "a//0"]
        self.assertTrue(TestUtils.check(input, expected, 211))


    def test_74(self):
        input=[
            "INSERT s string",
            "ASSIGN s '21'"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 212))

    def test_75(self):
        input=[
            "INSERT s string",
            "ASSIGN s a"
        ]
        expected = ["Undeclared: ASSIGN s a"]

        self.assertTrue(TestUtils.check(input, expected, 213))

    def test_76(self):
        input=[
            "INSERT s string",
            "ASSIGN s 'a 12 C'"
        ]
        expected = ["Invalid: ASSIGN s 'a 12 C'"]

        self.assertTrue(TestUtils.check(input, expected, 214))


    def test_77(self):
        input=[
            "INSERT s string",
            "ASSIGN s 'a 12 C'"
        ]
        expected = ["Invalid: ASSIGN s 'a 12 C'"]

        self.assertTrue(TestUtils.check(input, expected, 215))

    def test_78(self):
        input=[
           "INSERT\ta\tnumber"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 216))

    def test_79(self):
        input=[
            "INSERT \ta\tnumber"
        ]
        expected = ["Invalid: INSERT \ta\tnumber"]

        self.assertTrue(TestUtils.check(input, expected, 217))

    def test_80(self):
        input=[
            "\tINSERT a number"
        ]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 218))

    def test_81(self):
        input=[
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 219))