'''horoscope grabber service'''
import Horoscope


def write_to_file(my_horoscope, path):
    '''write to target file'''
    horoscope_page = open(path, 'w')
    horoscope_page.write(my_horoscope)
    horoscope_page.close()



def main():
    '''main'''
    my_horoscope = Horoscope.get_horoscope('scorpio', 'today')
    print(my_horoscope)
    write_to_file(my_horoscope, '/Users/tyler/Desktop/Dev/horoscope.html')


main()
