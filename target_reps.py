def calculate_optimal_weight(max_weight, max_reps, target_reps):
    # 最大レップ数から1RMを計算
    one_rep_max = max_weight * (1 + max_reps / 40)
    
    # 目標レップ数での最適重量を計算
    target_weight = one_rep_max / (1 + target_reps / 40)
    
    return target_weight

max_weight = 30  # 最大重量
max_reps = 20    # 最大レップ数
target_reps = 8  # 目標レップ数

optimal_weight = calculate_optimal_weight(max_weight, max_reps, target_reps)
print(f"限界8回の最適重量は約 {optimal_weight:.2f} kgです。")
