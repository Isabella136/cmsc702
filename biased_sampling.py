import numpy as np
import treeswift
import os

def path_to_tree(path):
    file = open(path)
    newick = file.read()
    file.close()
    tree = treeswift.read_tree_newick(newick)
    return(tree)

for inner_dir in ["high", "low", "mid"]:
    for replicate in range(1, 10):
        species_path = "".join(
            ("fix_samples/", inner_dir, "/0", str(replicate), "/s_tree.trees"))
        species_tree = path_to_tree(species_path)

        biased_sampling = np.random.uniform(low=5, high=20, size=50).tolist()
        label_set = {"0_0_0"}
        for sample in range(1,51):
            for indiv in range(int(round(biased_sampling[sample-1]))):
                label = "_0_".join((str(sample), str(indiv)))
                label_set.add(label)

        for gene in range(1, 10):
            gene_path = "".join(
                ("fix_samples/", inner_dir, "/0", str(replicate), "/g_trees000", str(gene), ".trees"))
            gene_tree = path_to_tree(gene_path)
            gene_tree = gene_tree.extract_tree_with(label_set)
            biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate), "/g_trees000", str(gene), ".trees"))
            biased_gene_dir = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate)))
            if not os.path.exists(biased_gene_dir):
                os.mkdir(biased_gene_dir)
            open(biased_gene_path, "w").close()
            gene_tree.write_tree_newick(biased_gene_path)

        for gene in range(10, 100):
            gene_path = "".join(
                ("fix_samples/", inner_dir, "/0", str(replicate), "/g_trees00", str(gene), ".trees"))
            gene_tree = path_to_tree(gene_path)
            gene_tree = gene_tree.extract_tree_with(label_set)
            biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate), "/g_trees00", str(gene), ".trees"))
            biased_gene_dir = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate)))
            if not os.path.exists(biased_gene_dir):
                os.mkdir(biased_gene_dir)
            open(biased_gene_path, "w").close()
            gene_tree.write_tree_newick(biased_gene_path)

        for gene in range(100, 1000):
            gene_path = "".join(
                ("fix_samples/", inner_dir, "/0", str(replicate), "/g_trees0", str(gene), ".trees"))
            gene_tree = path_to_tree(gene_path)
            gene_tree = gene_tree.extract_tree_with(label_set)
            biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate), "/g_trees0", str(gene), ".trees"))
            biased_gene_dir = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate)))
            if not os.path.exists(biased_gene_dir):
                os.mkdir(biased_gene_dir)
            open(biased_gene_path, "w").close()
            gene_tree.write_tree_newick(biased_gene_path)

        gene = 1000
        gene_path = "".join(
            ("fix_samples/", inner_dir, "/0", str(replicate), "/g_trees", str(gene), ".trees"))
        gene_tree = path_to_tree(gene_path)
        gene_tree = gene_tree.extract_tree_with(label_set)
        biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/0", str(replicate), "/g_trees", str(gene), ".trees"))
        biased_gene_dir = "".join(
            ("biased_samples/", inner_dir, "/0", str(replicate)))
        if not os.path.exists(biased_gene_dir):
            os.mkdir(biased_gene_dir)
        open(biased_gene_path, "w").close()
        gene_tree.write_tree_newick(biased_gene_path)
    
    for replicate in range(10, 21):
        species_path = "".join(
            ("fix_samples/", inner_dir, "/", str(replicate), "/s_tree.trees"))
        species_tree = path_to_tree(species_path)

        biased_sampling = np.random.uniform(low=5, high=20, size=50).tolist()
        label_set = {"0_0_0"}
        for sample in range(1,51):
            for indiv in range(int(round(biased_sampling[sample-1]))):
                label = "_0_".join((str(sample), str(indiv)))
                label_set.add(label)

        for gene in range(1, 10):
            gene_path = "".join(
                ("fix_samples/", inner_dir, "/", str(replicate), "/g_trees000", str(gene), ".trees"))
            gene_tree = path_to_tree(gene_path)
            gene_tree = gene_tree.extract_tree_with(label_set)
            biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate), "/g_trees000", str(gene), ".trees"))
            biased_gene_dir = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate)))
            if not os.path.exists(biased_gene_dir):
                os.mkdir(biased_gene_dir)
            open(biased_gene_path, "w").close()
            gene_tree.write_tree_newick(biased_gene_path)

        for gene in range(10, 100):
            gene_path = "".join(
                ("fix_samples/", inner_dir, "/", str(replicate), "/g_trees00", str(gene), ".trees"))
            gene_tree = path_to_tree(gene_path)
            gene_tree = gene_tree.extract_tree_with(label_set)
            biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate), "/g_trees00", str(gene), ".trees"))
            biased_gene_dir = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate)))
            if not os.path.exists(biased_gene_dir):
                os.mkdir(biased_gene_dir)
            open(biased_gene_path, "w").close()
            gene_tree.write_tree_newick(biased_gene_path)

        for gene in range(100, 1000):
            gene_path = "".join(
                ("fix_samples/", inner_dir, "/", str(replicate), "/g_trees0", str(gene), ".trees"))
            gene_tree = path_to_tree(gene_path)
            gene_tree = gene_tree.extract_tree_with(label_set)
            biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate), "/g_trees0", str(gene), ".trees"))
            biased_gene_dir = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate)))
            if not os.path.exists(biased_gene_dir):
                os.mkdir(biased_gene_dir)
            open(biased_gene_path, "w").close()
            gene_tree.write_tree_newick(biased_gene_path)

        gene = 1000
        gene_path = "".join(
            ("fix_samples/", inner_dir, "/", str(replicate), "/g_trees", str(gene), ".trees"))
        gene_tree = path_to_tree(gene_path)
        gene_tree = gene_tree.extract_tree_with(label_set)
        biased_gene_path = "".join(
                ("biased_samples/", inner_dir, "/", str(replicate), "/g_trees", str(gene), ".trees"))
        biased_gene_dir = "".join(
            ("biased_samples/", inner_dir, "/", str(replicate)))
        if not os.path.exists(biased_gene_dir):
            os.mkdir(biased_gene_dir)
        open(biased_gene_path, "w").close()
        gene_tree.write_tree_newick(biased_gene_path)