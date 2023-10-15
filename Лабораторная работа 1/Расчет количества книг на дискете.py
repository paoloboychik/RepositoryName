# TODO Найдите количество книг, которое можно разместить на дискете

memory = 1.44 * 1024 * 1024 # in bytes
pages = 100
strs = 50
symbols = 25
weigth_of_sym = 4

print("Количество книг, помещающихся на дискету:",
      round(memory // (pages*strs*symbols*weigth_of_sym)))
