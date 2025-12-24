import pandas as pd
import os

def process_excel_with_path(manual_path):
    clean_path = manual_path.strip('"')
    
    print(f"\n--- Targeted Processing: {os.path.basename(clean_path)} ---")
    
    if os.path.exists(clean_path):
        try:
            df = pd.read_excel(clean_path)
            
            # The WSP Risk Logic
            df['Risk_Score'] = df['Likelihood'] * df['Severity']
            df['Action_Level'] = df['Risk_Score'].apply(
                lambda x: "CRITICAL" if x >= 15 else ("MEDIUM" if x >= 8 else "LOW")
            )
            
            # Save to the same folder where your file is
            output_dir = os.path.dirname(clean_path)
            output_file = os.path.join(output_dir, 'wsp_final_results.xlsx')
            
            df.to_excel(output_file, index=False)
            print(f"Success! Final Report saved at: {output_file}")
            
        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print(f"Error: The path you pasted does not exist. Please check it.")

# --- EXECUTION ---
if __name__ == "__main__":
    # PASTE YOUR LINK BELOW INSIDE THE r" "
    # Example: my_link = r"C:\Users\Advika\Documents\wsp_data.xlsx"
    my_link = r"C:\Advika\Python\wsp_data.xlsx"
    
    if "PASTE_YOUR" in my_link:
        print("Wait! You need to paste your file path into the code first.")
    else:
        process_excel_with_path(my_link)
