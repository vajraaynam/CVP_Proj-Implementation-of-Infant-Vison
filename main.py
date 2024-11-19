# main.py
from workers import ContrastSensitivity, VisualAcuity, display_images
from torchvision import transforms
from eval_performance import evaluate_performance, plot_performance

def main():
    custom_transform = transforms.Compose([
    transforms.ToTensor(),
    ContrastSensitivity(age=16),  # Adjust age as required
    VisualAcuity(age=16)])  

    no_transform = [transforms.ToTensor()]

    display_images(transform=custom_transform, no_transform=no_transform)

    dauer_with_tranform = evaluate_performance(custom_transform, 'Infant Vision Transform')
    dauer_no_tranform = evaluate_performance(transforms.ToTensor(), 'No transforms') #quasi nur tensor umwandelung 

    performance_file = "performance_summary.txt"
    with open(performance_file, "w") as file:
        file.write(f"Time with transformations: {dauer_with_tranform:.2f} seconds\n")
        file.write(f"Time without transformations: {dauer_no_tranform:.2f} seconds\n")

    # Plot and save graph
    times = [dauer_with_tranform, dauer_no_tranform]
    labels = ['With Transformations', 'Without Transformations']
    plot_performance(times, labels, 'performance_comparison.png')

    


    return performance_file, 'performance_comparison.png'

    
if __name__ == "__main__":
    main()

