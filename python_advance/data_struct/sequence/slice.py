"""列表、元组、字符串等所有序列类型都支持切片操作"""


class Slice:
    def slice(self):
        s = [10, 20, 30, 40, 50, 60]
        print(s[:2])
        print(s[2:])

    def slice_object(self):
        """表示步长"""
        s = "bicycle"
        print(s[::3])
        print(s[::-1])
        print(s[::-2])

    def slice_name(self):
        invoice = """
        ... 
        0.....6.................................40........52...55........
        ... 1909  Pimoroni PiBrella                     $17.50    3    $52.50
        ... 1489  6mm Tactile Switch x20                 $4.95    2     $9.90
        ... 1510  Panavise Jr. - PV-201
        $28.00    1    $28.00
        ... 1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
        ..."""

        """可以为变量命名"""
        SKU = slice(0, 6)
        DESCRIPTION = (6, 40)
        UNIT_PRICE = (40, 52)
        QUANTITY = (52, 55)
        ITEM_TOTAL = (55, None)

        line_items = invoice.split("\n")[2:]
        for item in line_items:
            print(item[UNIT_PRICE], item[DESCRIPTION])

    def demo(self):
        self.slice()
        self.slice_object()


s_demo = Slice()
s_demo.demo()
