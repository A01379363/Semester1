while True:
    pesos_mex = float(input("MXN$"))
    currency = input("Which currency would you like to convert to (Euros, USD or CAD)? ")
    euros = pesos_mex*.047
    usd = pesos_mex*.052
    cad = pesos_mex*.068
    if currency.lower() == "euros":
        print(f"€{euros}")
    elif currency.lower() == "usd":
        print(f"USD${usd}")
    elif currency.lower() == "cad":
        print(f"CAD${cad}")
    exit = input("Exit? ")
    if exit.lower() == "yes":
        break
