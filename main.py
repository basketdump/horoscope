'''horoscope grabber service'''
import Horoscope


def write_to_file(my_horoscope, path):
    '''write to target file'''
    horoscope_page = open(path, 'w')
    horoscope_page.write(my_horoscope)
    horoscope_page.close()



def main():
    '''please change sign, day, and html path to fit your needs'''
    sign = 'scorpio'
    day = 'today' # can be 'today', 'yesterday', or 'tomorrow'
    file_path = '/Users/tyler/Desktop/Dev/horoscope.html'

    my_horoscope = Horoscope.get_horoscope(sign, day)
    print(my_horoscope)
    write_to_file(my_horoscope, file_path)


main()
