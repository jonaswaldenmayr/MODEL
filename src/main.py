from parameters import params
import numpy as np

from plotting import plot_time_series



def main():
    print('Starting model...')

    ### Initialize Arrays ###
    #Economy
    num_timesteps = int(params.t_max / params.step_size)   # Calculate actual number of steps
    Y = np.zeros(num_timesteps)
    K = np.zeros(num_timesteps)
    A = np.zeros(num_timesteps)
    C = np.zeros(num_timesteps)
    k = np.zeros(num_timesteps+1)
    #x = np.zeros(num_timesteps)
    #Climate
    D = np.zeros(num_timesteps)
    M = np.zeros(num_timesteps+1)
    E = np.zeros(num_timesteps)

    ### Calibration ###


    ### Calculate Shadow Values ###
    phi_k = params.kappa / (1-(params.beta * params.kappa))   # Shadow Value of logK
    phi_M = -(params.xi * (1 + (params.beta * phi_k)))/(1 - (params.beta * (1-params.delta)))    # Shadow Value of Carbon

    ### Calculate Control Values ###
    x_opti = 1 / (1 + (params.beta * phi_k))      #optimal consumption rate
    E_opti = (params.nu * (1 + params.beta * phi_k)) / (params.beta * (-phi_M))      #optimal emissions 

    print(f'\nModel parameters:\n{params}\n')
    print(f"phi_k = {phi_k}")
    print(f"phi_m = {phi_M}")
    print(f"x_opti = {x_opti}")
    print(f"E_opti = {E_opti}")

    #####################
    ### Run the model ###

    print("\n\nFirst Decade")
    ## first iteration (frist decade) and initialization ##
    #Climate
    M[0] = params.M_init
    D[0] = 1 - np.exp(-params.xi * M[0])
    E[0] = E_opti
    #Economy
    K[0] = params.K_init
    A[0] = params.A_init
    Y[0] = params.Y_init
    C[0] = x_opti * Y[0] * (1-D[0])
    k[0] = np.log(K[0]) 
    # equations of motion
    k[1] = (np.log(A[0])) + (params.kappa * k[0]) + (params.nu * (np.log(E[0]))) - (params.xi * M[0]) + np.log(1 - x_opti) #using control value x_opti
    M[1] = (1-params.delta) * M[0] + E[0]


    print(f"Y[0] = {Y[0]}")
    print(f"K[0] = {K[0]}")
    print(f"D[0] = {D[0]}")
    print(f"M[0] = {M[0]}")


    # Loop starts from index 1
    for i, t in enumerate(range(10, params.t_max, params.step_size), start=1):

        print(f"\nYear {t}")
       
        E[i] = E_opti+ 2 ############## ADJUST ##############
        D[i] = 1 - np.exp(-params.xi * M[i])

        K[i] = np.exp(k[i])
        A[i] = A[i-1] * (1 + params.tech_improvement_rate)
        Y[i] = A[i] * K[i]**params.kappa * E[i]**params.nu  
        C[i] = x_opti * (Y[i] * (1-D[i]))

        
       
        ## equations of motion
        k[i+1] = (np.log(A[i])) + (params.kappa * k[i]) + (params.nu * (np.log(E[i]))) - (params.xi * M[i]) + np.log(1 - x_opti) #using control value x_opti
        M[i+1] = (1-params.delta) * M[i] + E[i]


        print(f"Y[i] = {Y[i]}")
        print(f"K[i] = {K[i]}")
        print(f"D[i] = {D[i]}")
        print(f"M[i] = {M[i]}")



    

    plot_time_series( Y, title="GDP Y")
    plot_time_series( K, title="K")
    plot_time_series( D, title="D")
    plot_time_series( M, title="Athmospheric Carbon")



if __name__ == "__main__":
    main()

