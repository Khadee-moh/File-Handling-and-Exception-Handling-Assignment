def process_file():
    filename = input("Enter the name of the file to read (e.g., input.txt): ")

        
        with open(filename, 'r') as file:
            content = file.read()
 
        modified_content = content.title()

 
        output_filename = f"modified_{filename}"

        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"❌ Error: The file '{filename}' could not be read or written.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the function
process_file()
