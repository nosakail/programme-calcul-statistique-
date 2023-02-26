def calculer_moyenne(liste):
    """
    Cette fonction calcule la moyenne d'une liste de nombres.
    """
    total = sum(liste)
    moyenne = total / len(liste)
    return moyenne

def calculer_variance(liste):
    """
    Cette fonction calcule la variance d'une liste de nombres.
    """
    moyenne = calculer_moyenne(liste)
    variance = sum((x - moyenne) ** 2 for x in liste) / len(liste)
    return variance

def covariance(X, Y):
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    cov = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / (n - 1)
    return cov



def ecart_type(X):

    variance_X = calculer_variance(X)
    std_dev_X = math.sqrt(variance_X)
    return std_dev_X

def correlation(X, Y):
    cov_XY = covariance(X, Y)
    std_dev_X = ecart_type(X)
    std_dev_Y = ecart_type(Y)
    correlation_XY = cov_XY / (std_dev_X * std_dev_Y)
    return correlation_XY

def regression(X, Y):
    mean_X = calculer_moyenne(X)
    mean_Y = calculer_moyenne(Y)
    cov_XY = covariance(X, Y)
    var_X = calculer_variance(X)
    slope = cov_XY / var_X
    intercept = mean_Y - slope * mean_X
    return (slope, intercept)

def predict_y(x, X, Y):
    slope, intercept = regression(X, Y)
    y_pred = slope * float(x) + intercept
    return y_pred



if __name__ == "__main__":
    #venez follow twitter : @nosakail 

    import matplotlib.pyplot as plt
    #intaller la bibliotheque matplotlib -> pip install matplotlib
    import math

    #faire un nuage de point 
    x = [1, 2, 3, 4, 5] #changer selon vos valeurs
    y = [6.25, 6.71,7.04,7.75,8.33]  #changer selon vos valeurs

    plt.figure()

    plt.scatter(x, y)
   
    plt.title('Nuage de points')

    plt.xlabel('temps t') #axe x
    plt.ylabel('concentration C') #axe y

    plt.show()


    #Calcul des moyennes 
    valeur_x = [1, 2, 3, 4, 5]
    valeur_y = [6.25, 6.71,7.04,7.75,8.33]
    moyenne_x = calculer_moyenne(valeur_x)
    moyenne_y = calculer_moyenne(valeur_y)
    print("xbar = ", moyenne_x)
    print("ybar = ", moyenne_y)

    # calcul de la varience
    variance_x = calculer_variance(valeur_x)
    print("var(x) = ", variance_x)
    variance_y = calculer_variance(valeur_y)
    print("var(y) = ", variance_y)

    #calcul de la covarience
    covariance_XY = covariance(valeur_x, valeur_y)
    print("La cov(x,y) = ", covariance_XY)

    #calcul de l'ecart type
    ecart_type_X = ecart_type(valeur_x)
    print("L'écart-type de X est :", ecart_type_X)
    ecart_type_Y = ecart_type(valeur_y)
    print("L'écart-type de Y est :", ecart_type_Y)

    #calcul du coefficient de correlation 
    corr_XY = correlation(valeur_x, valeur_y)
    print("Le coefficient de corrélation entre X et Y est :", corr_XY)

    #determiner l'equation de la droite de regression 
    slope, intercept = regression(valeur_x, valeur_y)
    print("L'équation de la droite de régression est : y = ", slope, "x + ", intercept)

    #estimation d'une valeur
    estimation_pour_x = 6 #changer selon votre valeur

    y_pred = predict_y(estimation_pour_x, valeur_x, valeur_y)
    print("La valeur de y prédite pour x =", x, "est", y_pred)
