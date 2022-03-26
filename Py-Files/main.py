import literales as msg
import functions as f
import nilib


def main():
    ans = 0
    x = nilib.validate(msg.MENU, 1, 2)
    match x:
        case 1:
            file = input(msg.MSG0)
            f_name = f.val_file(file, msg.EXT2)
            f.rd_dict(f_name)
        case _:
            file = input(msg.MSG0)
            f_name = f.val_file(file, msg.EXT2)
            head = f.check_file(f_name)
            if head == 1:
                ans = nilib.validate(msg.MSG1, 0, 1)
            if ans == 1:
                f.add_dict(f_name, head, 'w')
            else:
                f.add_dict(f_name, head, 'a')


if __name__ == '__main__':
    main()
