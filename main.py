import data
import sys
import agglomerative_clustering
import link

def main(argv):
    #  q1

    the_data = data.Data("Leukemia_sample.csv")
    samples = the_data.create_samples()
    the_data.create_distance_matrix(samples)
    single_link = agglomerative_clustering.AgglomerativeClustering(link.SingleLink(), samples)    
    single_link.run(7)
    print()
    complete_link = agglomerative_clustering.AgglomerativeClustering(link.CompleteLink(), samples)
    complete_link.run(7)


if __name__ == '__main__':
    main(sys.argv)
