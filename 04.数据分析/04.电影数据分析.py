import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# ==================== 配置区域 ====================
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.rcParams['figure.dpi'] = 100  # 设置默认分辨率

# 配色方案
COLORS = {
    'primary': '#2196F3',
    'secondary': '#FF9800',
    'success': '#4CAF50',
    'danger': '#F44336',
    'gradient_start': '#667eea',
    'gradient_end': '#764ba2'
}


def load_data(filepath='data/movie.csv'):
    """加载数据并进行基本清洗"""
    df = pd.read_csv(filepath)
    print(f"数据加载成功！共 {len(df)} 条记录")
    print(f"\n数据基本信息：")
    print(df.info())
    print(f"\n缺失值统计：")
    print(df.isnull().sum())
    return df


def analyze_year_distribution(df):
    """分析电影年份分布"""
    year_counts = df.groupby('年份').size()
    
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # 准备数据
    years = year_counts.index.tolist()
    counts = year_counts.values.tolist()
    
    # 绘制折线图（带面积填充）
    ax.plot(years, counts, color=COLORS['primary'], linewidth=2.5, 
            marker='o', markersize=4, label='电影数量', zorder=3)
    ax.fill_between(years, counts, alpha=0.15, color=COLORS['primary'])
    
    # 添加峰值标注
    max_year = year_counts.idxmax()
    max_count = year_counts.max()
    ax.annotate(f'峰值: {max_count}部\n{max_year}年', 
                xy=(max_year, max_count), 
                xytext=(max_year + 10, max_count * 0.9),
                arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=2),
                fontsize=11, color=COLORS['danger'],
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    # 设置标题和标签
    ax.set_title('电影年份分布趋势图', fontsize=20, fontweight='bold', pad=20)
    ax.set_xlabel('年份', fontsize=14, labelpad=10)
    ax.set_ylabel('电影数量（部）', fontsize=14, labelpad=10)
    
    # 优化刻度
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=20))
    ax.tick_params(axis='both', labelsize=11)
    
    # 添加网格
    ax.grid(True, linestyle='--', alpha=0.3, color='gray')
    ax.set_axisbelow(True)  # 网格在底层
    
    # 添加图例
    ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('year_distribution.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("✓ 年份分布图已保存为 year_distribution.png")


def analyze_top_movies(df, top_n=10):
    """分析评分最高的电影"""
    if '评分' in df.columns:
        top_movies = df.nlargest(top_n, '评分')[['名称', '评分', '年份']]
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # 横向柱状图
        bars = ax.barh(range(len(top_movies)), top_movies['评分'].values,
                      color=plt.cm.viridis(np.linspace(0.3, 0.9, len(top_movies))),
                      edgecolor='white', linewidth=1.5)
        
        # 设置y轴标签
        ax.set_yticks(range(len(top_movies)))
        ax.set_yticklabels(top_movies['名称'].values, fontsize=11)
        ax.invert_yaxis()  # 最高分在上面
        
        # 在柱子上添加数值标签
        for i, (bar, score) in enumerate(zip(bars, top_movies['评分'].values)):
            ax.text(score + 0.1, i, f'{score:.1f}', 
                   va='center', fontsize=10, fontweight='bold')
        
        ax.set_title(f'TOP {top_n} 高分电影排行榜', fontsize=20, fontweight='bold', pad=20)
        ax.set_xlabel('评分', fontsize=14, labelpad=10)
        ax.set_xlim(0, 10)
        
        ax.grid(axis='x', linestyle='--', alpha=0.3)
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        plt.savefig('top_movies.png', dpi=150, bbox_inches='tight')
        plt.show()
        print(f"✓ TOP{top_n}电影排行榜已保存为 top_movies.png")
        return top_movies


def create_dashboard(df):
    """创建综合数据看板"""
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))
    fig.suptitle('电影数据综合分析看板', fontsize=24, fontweight='bold', y=0.98)
    
    # 1. 年份分布（左上）
    ax1 = axes[0, 0]
    year_counts = df.groupby('年份').size()
    ax1.plot(year_counts.index, year_counts.values, color=COLORS['primary'], 
             linewidth=2, marker='.', markersize=3)
    ax1.fill_between(year_counts.index, year_counts.values, alpha=0.2, color=COLORS['primary'])
    ax1.set_title('年份分布', fontsize=14, fontweight='bold')
    ax1.set_xlabel('年份')
    ax1.set_ylabel('数量')
    ax1.grid(True, linestyle='--', alpha=0.3)
    
    # 2. 评分分布（右上）
    ax2 = axes[0, 1]
    if '评分' in df.columns:
        scores = df['评分'].dropna()
        ax2.hist(scores, bins=30, color=COLORS['secondary'], 
                edgecolor='white', alpha=0.7, density=True)
        ax2.axvline(scores.mean(), color=COLORS['danger'], 
                   linestyle='--', linewidth=2, label=f'平均分: {scores.mean():.2f}')
        ax2.set_title('评分分布', fontsize=14, fontweight='bold')
        ax2.set_xlabel('评分')
        ax2.set_ylabel('密度')
        ax2.legend()
        ax2.grid(True, linestyle='--', alpha=0.3, axis='y')
    
    # 3. 关键指标（左下）
    ax3 = axes[1, 0]
    ax3.axis('off')
    stats_text = f"""
    数据概览
    {'='*30}
    总电影数: {len(df):,} 部
    年份范围: {df['年份'].min()} - {df['年份'].max()}
    平均评分: {df['评分'].mean():.2f}
    最高评分: {df['评分'].max():.1f}
    最低评分: {df['评分'].min():.1f}
    {'='*30}
    """
    ax3.text(0.1, 0.5, stats_text, fontsize=12, family='monospace',
            verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # 4. 年代统计（右下）
    ax4 = axes[1, 1]
    df['年代'] = (df['年份'] // 10) * 10
    decade_counts = df.groupby('年代').size()
    colors_bar = plt.cm.coolwarm(np.linspace(0.2, 0.8, len(decade_counts)))
    bars = ax4.bar(decade_counts.index.astype(str), decade_counts.values,
                  color=colors_bar, edgecolor='white', linewidth=1.5)
    ax4.set_title('各年代电影数量', fontsize=14, fontweight='bold')
    ax4.set_xlabel('年代')
    ax4.set_ylabel('数量')
    ax4.tick_params(axis='x', rotation=45)
    ax4.grid(True, linestyle='--', alpha=0.3, axis='y')
    
    # 在柱子上添加数值
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('movie_dashboard.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("✓ 综合看板已保存为 movie_dashboard.png")


def main():
    """主函数"""
    print("=" * 50)
    print("电影数据分析系统")
    print("=" * 50)
    
    # 1. 加载数据
    df = load_data()
    
    # 2. 分析年份分布
    print("\n正在生成年份分布图...")
    analyze_year_distribution(df)
    
    # 3. 分析高分电影
    if '评分' in df.columns:
        print("\n正在生成TOP电影排行榜...")
        top_movies = analyze_top_movies(df, top_n=10)
        print("\nTOP 10 电影列表：")
        print(top_movies.to_string(index=False))
    
    # 4. 创建综合看板
    print("\n正在生成综合数据看板...")
    create_dashboard(df)
    
    print("\n" + "=" * 50)
    print("分析完成！所有图表已保存。")
    print("=" * 50)


if __name__ == '__main__':
    main()
