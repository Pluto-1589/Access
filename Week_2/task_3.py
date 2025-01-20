def get_price(price_cone,
              num_scoops_vanilla, price_per_scoop_vanilla,
              num_scoops_chocolate, price_per_scoop_chocolate):

    return price_cone + (num_scoops_vanilla * price_per_scoop_vanilla) + (num_scoops_chocolate * price_per_scoop_chocolate)


print(get_price(0.50, 1, 1.20, 2, 1.20))
