

###### Parameters ######
########################
class ModelParameters:
    def __init__(self):
        # Time parameters
        self.step_size = 10
        self.num_decades = 3
        self.t_max = self.step_size * self.num_decades

        ### Economy ### 
        # Starting Values (1 = 1 Trillion USD)
        self.Y_init = 130
        self.A_init = 20                                ############## ADJUST ##############
        self.K_init = 3*self.Y_init
        # Parameters
        self.nu = 0.07                  #emission dependency parameter
        self.kappa = 0.3                #capital elasticity?
        self.beta = 0.84                #consider using formula in ACE paper
        self.tech_improvement_rate = 0.18               ############## ADJUST ##############

        self.prtp = 0.013896            # Pure rate of time preference -> currently not used
        # self.beta = 1 / (1 + self.prtp)**self.step_size  # Discount factor for 10-year steps

        ### Climate ###
        # Starting Values
        ppm_value = 427                 #see Mauna Loa data
        conversion_factor = 2.31        #ppm to GtC
        self.M_init = ppm_value * conversion_factor
        # Parameters
        self.xi = 0.0002046             #damage parameter; see Golosov_2014 
        self.delta = 0.01               #removal rate
       
    def __repr__(self):
        """Returns a string representation of all parameters"""
        return '\n'.join(f'{key} = {value}' for key, value in vars(self).items())

# Create an instance of ModelParameters
params = ModelParameters()



