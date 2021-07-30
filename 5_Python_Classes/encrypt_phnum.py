class ShrinkNumber():
    def __init__(self, str_num):
        self.str_num = str_num
        print("Original Phone number : {}".format(self.str_num))
        self.total_splits_ = []
        # method calling to get the splits of the number based on the condition
        self.refine_nums()
    
    def split_nums(self, str_value):
        sum_ = 0
        count_ = 0
        
        if (int(str_value[0]) % 2 == 0):
            # if the num is even
            for i in range(1, len(str_value) + 1):
                sum_ += int(str_value[i - 1])
                count_ += 1
                if ((sum_ % 2) != 0):
                    self.total_splits_.append(str_value[:count_])
                    # recursive method calling
                    return self.split_nums(str_value[count_:])
        else:
            # if the num is odd
            for i in range(1, len(str_value) + 1):
                sum_ += int(str_value[i - 1])
                count_ += 1
                if ((sum_ % 2) == 0):
                    self.total_splits_.append(str_value[:count_])
                    # recursive method calling
                    return self.split_nums(str_value[count_:])
    
    def refine_nums(self):
        # check if the length of the number is 10
        if len(self.str_num) == 10:
            e = self.str_num[len(self.str_num) - 1]
            try:
                self.split_nums(str_value=self.str_num)
                self.total_splits_.append(e)
            except Exception as f:
                return "This number is not valid"
        # returning the statement when condition doesn't match
        return "Number exceeds the limit 10"
    
    def resolve_number(self, num_list):
        manipulated_ = ''
        for i in num_list:
            # summing up each split num after coverting it into int() and reconverting into str()
            manipulated_ += str(sum([int(j) for j in list(i)]))
        return manipulated_
    
    def shrinked(self):
        if self.total_splits_:
            # method calling to return the shrinked number
            return self.resolve_number(num_list=self.total_splits_)
        else:
            return 'Invalid number'


if __name__ == '__main__':
    phone_number = input("Enter phone number: ")
    new_num = ShrinkNumber(str_num=phone_number)
    print("Total splits by odd and even : {}".format(new_num.total_splits_))
    print("Shrinked number : {}".format(new_num.shrinked()))