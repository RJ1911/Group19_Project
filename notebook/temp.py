import os
import csv

def combine_files(txt_dir, lab_dir, output_csv, num_files=29783):
    """
    Combines the contents of paired .txt and .lab files named identically into a CSV file, limiting processing to a specified number of files and writing content to separate columns.

    Args:
        txt_dir (str): Directory containing the .txt files.
        lab_dir (str): Directory containing the .lab files.
        output_csv (str): Path to the output CSV file.
        num_files (int, optional): Number of files to process. Defaults to 100.
    """

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["category", "resume"])  # Write header row with desired order

        for filename in os.listdir(txt_dir)[:num_files]:
            if not filename.endswith(".txt"):
                continue  # Skip non-text files

            txt_path = os.path.join(txt_dir, filename)
            lab_path = os.path.join(lab_dir, filename.replace(".txt", ".lab"))

            if not os.path.exists(lab_path):
                print(f"Error: Pair of .lab file not found for {filename}")
                continue

            try:
                with open(txt_path, "r") as txt_file, open(lab_path, "r") as lab_file:
                    resume_text = txt_file.read().strip()
                    category_text = lab_file.readline().strip()
                    writer.writerow([category_text, resume_text])
            except FileNotFoundError:
                print(f"Error: Pair of files not found for {filename}")

if __name__ == "__main__":
    txt_dir = "C:\\Users\Dell\Desktop\Final Year\\resumes_corpus"  # Replace with your directory path
    lab_dir = "C:\\Users\Dell\Desktop\Final Year\\resumes_corpus"  # Replace with your directory path
    output_csv = "combined_data.csv"

    combine_files(txt_dir, lab_dir, output_csv)
    print("CSV file created successfully!")
