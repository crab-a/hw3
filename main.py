import data
import sys


def main(argv):
    #  q1
    print('Question 1:')
    the_data = data.Data("Leukemia_sample.csv")
    samples = the_data.create_samples()
    the_data.create_distance_matrix(samples)
    print(the_data.distance_matrix[0][1])



if __name__ == '__main__':
    main(sys.argv)