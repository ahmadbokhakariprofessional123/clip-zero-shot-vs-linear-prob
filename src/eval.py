import numpy as np


def per_class_recall(true_labels, preds, num_classes=10):
    recalls = []
    for cls in range(num_classes):
        idx = np.where(true_labels == cls)[0]
        recalls.append((preds[idx] == cls).mean())
    return np.array(recalls)



def per_class_recall_1_and_5(sim_matrix, true_labels, class_names):
    recall1 = {}
    recall5 = {}

    top5 = np.argsort(sim_matrix, axis=1)[:, -5:]

    for cls_idx, cls_name in enumerate(class_names):
        idx = np.where(true_labels == cls_idx)[0]

        recall1[cls_name] = np.mean(np.argmax(sim_matrix[idx], axis=1) == cls_idx)
        recall5[cls_name] = np.mean([cls_idx in top5[i] for i in idx])

    return recall1, recall5


def topk_retrieval(sim_matrix, k=5):
    sim_t2i = sim_matrix.T
    return np.argsort(sim_t2i, axis=1)[:, -k:][:, ::-1]
