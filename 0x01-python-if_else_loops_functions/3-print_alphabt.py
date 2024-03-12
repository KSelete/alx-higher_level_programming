#!/usr/bin/python3
for i in list(
        range(ord('a'), ord('e'))
        ) + list(
                range(ord('f'), ord('q'))
                ) + list(
                        range(ord('r'), ord('z') + 1)
                        ):
                    print('Last digit of {} is {} and is {}'.format(number, d,
                                                'greater than 5' if d > 5 else 
                                                'less than 6 and not 0' if d else 
                                                '0'))
