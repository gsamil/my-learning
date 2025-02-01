# Approximate Nearest Neighbor Methods

## Introduction

Nearest Neighbor Search (NNS) is an optimization problem of finding the point in a given set that is closest to a given point \[[1](https://en.wikipedia.org/wiki/Nearest_neighbor_search)\]. In practical applications, it can be used for classification, unsupervised clustering and similar proximity search problems. For some cases, we may need to find $k$ nearest neighbors instead of only one; in this case it's called k-Nearest Neighbor (kNN) There are a number of different methods of NNS, and they are divided into mainly two groups:

**1. Exact Methods :** These methods aims to find the exact closest point (or $k$ points) to a given point. So for each given point, we need to compute the distance with each point in the dataset. This means it has $O[n]$ time complexity, where $n$ is the number of samples in the dataset. For large datasets, exact methods become impractical as it's not possible to run the same computations each time there is a new sample.

**2. Approximate Methods :** For the above reason, approximate methods are developed. These methods tries to reduce the runtime of exact methods by sacrificing some level of accuracy. Therefore they are called approximate. Considering that for most of the real world scenarios we don't need an exact point, approximate solutions becomes a preferable alternative, as they generally run on $O[log(n)]$ runtime, where $n$ is the number of samples in the dataset.

My focus will be about approximate nearest neighbor (ANN) methods. There are a number of different ANN methods defined in the literature. Most of them are based on dividing the dataset into sub-groups, then searching only among the related sub-groups to increase the speed of search. There are a number of different ANN techniques.

## ANN Methods

### Hierarchical Navigable Small World (HNSW) Graphs

HNSW is a "Proximity Graph Method", which is considered to be the current state-of-the-art among the available ANN search methods.

It starts by building a graph where each node represents a data point and connections between them the similarity. There are multiple layers of this list (thus hierarchical), with the top layers containing fewer nodes&connections (so have a coarse view of the broader data) and bottom layers with more nodes&connections (but focused on a portion of the data). If you are familiar with skip lists \[[2](https://en.wikipedia.org/wiki/Skip_list)\], you will notice that logic of the HNSW is quite similar to it. So essentially this skip-list like structure makes it easily navigable.

### Locality Sensitive Hashing (LSH)

LSH is a "Hashing Based Method", where the aim is to put the similar items into the same bucket with high probability. It's effective because its runtime is independent of the dimension of the samples \[[3](https://www.cs.cmu.edu/~agray/approxnn.pdf)\].

### Approximate Nearest Neighbors Oh Yeah (ANNOY)

ANNOY is a "Tree Based Method". Tree based methods (KD-Trees, Random Projection Trees etc.) works by building a tree structure from the dataset. So we first select 2 samples from the dataset, and split the space into two using the equidistant plane of these 2 samples. Then we iteratively continue splitting the space into sub-trees until we reach the required granularity in our dataset. This is called "partitioning", then given a data sample, we can "search" this tree using simple guided DFS algorithms.

ANNOY creates a forest of these trees to improve the memory usage and runtime.

### Spill Trees

In contrast to the usual tree based methods, sub-trees in a spill tree can "spill over" onto each other. This essentially means some of the samples in the dataset will belog to multiple sub-trees in the final tree. In the tree structure, sometimes some close samples are divided by a plane and they fall under different sub-trees. Overlapping boundaries solves this problem by assigning these samples to multiple sub-trees, thus increases accuracy.

## ANN Python Libraries

I didn't try these libraries myself but I think they are useful guides to understand more about the implementations of the above methods.

- [**annoy**](https://github.com/spotify/annoy) implements the ANNOY algorithm.
- [**flann**](https://github.com/flann-lib/flann) is a library for performing fast approximate nearest neighbor searches in high dimensional spaces. It contains a collection of algorithms.
- [**nmslib**](https://github.com/nmslib/nmslib) is an efficient cross-platform similarity search library and a toolkit for evaluation of similarity search methods. It contains a collection of algorithms including HNSW.

## Conclusion

In this blog, I delved into the concept of Approximate Nearest Neighbor (ANN) methods, their importance, and some of the primary techniques used in this domain. ANN methods are crucial in handling large datasets where exact methods become impractical due to their high time complexity. They offer a balance between accuracy and computational efficiency, making them a preferred choice in many real-world scenarios.

I discussed several ANN methods such as Hierarchical Navigable Small World (HNSW) Graphs, Locality Sensitive Hashing (LSH), Approximate Nearest Neighbors Oh Yeah (ANNOY), and Spill Trees. Each of these methods has its unique approach to the problem.

However, the field of ANN is vast and continually evolving. There are numerous other methods that I haven't covered in this blog. Each of these methods targets a specific aspect of the nearest neighbor search problem and attempts to enhance it. Some focus on reducing computational complexity, others on improving accuracy, and some strive for a balance between both. As the field continues to grow, we can expect to see new methods and improvements on existing ones, further pushing the boundaries of what is possible in nearest neighbor search. It's an exciting time to be involved in this area of research and I look forward to seeing where it goes next.


## References

1. [Nearest Neighbor Search - Wikipedia](https://en.wikipedia.org/wiki/Nearest_neighbor_search)
2. [Skip Lists - Wikipedia](https://en.wikipedia.org/wiki/Skip_list)
3. [An Investigation of Practical Approximate Nearest Neighbor Algorithms - Paper](https://www.cs.cmu.edu/~agray/approxnn.pdf)
4. [Hierarchical Navigable Small Worlds - Medium](https://srivatssan.medium.com/hierarchical-navigable-small-worlds-d44d39d91f4b)
5. [A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search](https://arxiv.org/pdf/2101.12631.pdf)
6. [Nearest neighbors and vector models – part 2 – algorithms and data structures](https://erikbern.com/2015/10/01/nearest-neighbors-and-vector-models-part-2-how-to-search-in-high-dimensional-spaces.html)
7. [The Potential of Approximate Nearest Neighbors (ANN) in High-Dimensional Spaces - Medium](https://medium.com/@brijesh_soni/the-potential-of-approximate-nearest-neighbors-ann-in-high-dimensional-spaces-579567e4f1a7)
