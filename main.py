import data
import sys
import agglomerative_clustering
import link


def main(argv):
    #  q1
    MAX_CLUSTER = 7

    the_data = data.Data(argv[1])
    samples = the_data.create_samples()
    the_data.create_distance_matrix(samples)
    single_link = agglomerative_clustering.AgglomerativeClustering(link.SingleLink(), samples)
    single_link.run(MAX_CLUSTER)
    print()
    complete_link = agglomerative_clustering.AgglomerativeClustering(link.CompleteLink(), samples)
    complete_link.run(MAX_CLUSTER)


if __name__ == '__main__':
    main(sys.argv)
