import matplotlib.pyplot as plt
import matplotlib.patches as patches
from solution import Solution, data # Assuming solution.py is in the same directory

class Visualizer:
    def __init__(self, solution_instance):
        self.solution = solution_instance
        self.data = solution_instance.data
        self.xs = solution_instance.xs
        self.ys = solution_instance.ys
        self.edge_map_x = solution_instance.edge_map_x
        self.edge_map_y = solution_instance.edge_map_y

    def plot_points(self, ax):
        x_coords = [p[0] for p in self.data]
        y_coords = [p[1] for p in self.data]
        ax.plot(x_coords, y_coords, 'o-', color='blue', markersize=5, linewidth=1, label='Path Points')

    def plot_edges(self, ax):
        # Plot horizontal segments
        for x_val, y_range in self.edge_map_x.items():
            if y_range[0] != float('inf') and y_range[1] != float('-inf'):
                ax.plot([x_val, x_val], [y_range[0], y_range[1]], ':', color='gray', linewidth=0.5)
        # Plot vertical segments
        for y_val, x_range in self.edge_map_y.items():
            if x_range[0] != float('inf') and x_range[1] != float('-inf'):
                ax.plot([x_range[0], x_range[1]], [y_val, y_val], ':', color='gray', linewidth=0.5)

    def plot_rectangle(self, ax, p1, p2, color='red', alpha=0.3, label=None):
        min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
        min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        rect = patches.Rectangle((min_x - 0.5, min_y - 0.5), width, height,
                                 linewidth=1, edgecolor=color, facecolor=color, alpha=alpha, label=label)
        ax.add_patch(rect)

    def visualize_solution(self, part=1):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_aspect('equal', adjustable='box')

        self.plot_points(ax)
        # self.plot_edges(ax) # Uncomment to visualize edge maps

        max_area = 0
        best_rect = None

        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                p1 = self.data[i]
                p2 = self.data[j]
                
                is_valid = True
                if part == 2:
                    is_valid = self.solution.valid_rect(p1, p2)

                if is_valid:
                    current_area = self.solution.get_area(p1, p2)
                    if current_area > max_area:
                        max_area = current_area
                        best_rect = (p1, p2)
        
        if best_rect:
            self.plot_rectangle(ax, best_rect[0], best_rect[1], color='red', alpha=0.3, label=f'Max Area ({max_area})')
            
            # Highlight the points forming the best rectangle
            ax.plot(best_rect[0][0], best_rect[0][1], 'o', color='green', markersize=8, label='Rectangle Corner')
            ax.plot(best_rect[1][0], best_rect[1][1], 'o', color='green', markersize=8)


        # Set plot limits and labels
        all_x = [p[0] for p in self.data]
        all_y = [p[1] for p in self.data]
        
        if all_x and all_y:
            min_x, max_x = min(all_x), max(all_x)
            min_y, max_y = min(all_y), max(all_y)
            
            x_range = max_x - min_x
            y_range = max_y - min_y
            
            padding_x = max(1, x_range * 0.1)
            padding_y = max(1, y_range * 0.1)
            
            ax.set_xlim(min_x - padding_x, max_x + padding_x)
            ax.set_ylim(min_y - padding_y, max_y + padding_y)

        ax.set_xlabel('X-coordinate')
        ax.set_ylabel('Y-coordinate')
        ax.set_title(f'Day 09 - Part {part} - Max Rectangle Visualization')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        plt.show()

# Main execution
if __name__ == '__main__':
    s = Solution(data)
    visualizer = Visualizer(s)

    print('Visualizing Part 1...')
    visualizer.visualize_solution(part=1)
    print('Visualizing Part 2...')
    visualizer.visualize_solution(part=2)
