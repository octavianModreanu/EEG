import os
from bids.layout import BIDSLayout

def validate(dataset_path):
    """
    Lightweight validation using pybids to check the dataset structure,
    required files, and metadata completeness.
    """
    try:
        layout = BIDSLayout(dataset_path)

        print("Dataset successfully loaded. Checking for required files and metadata...")

        # Check required top-level files
        required_files = ['dataset_description.json', 'participants.tsv']
        for file in required_files:
            if not os.path.exists(os.path.join(dataset_path, file)):
                print(f"Error: Missing required file {file}")
                return False

        # Check metadata for functional files
        bold_files = layout.get(suffix='bold', extension='nii.gz')
        for bold_file in bold_files:
            metadata = layout.get_metadata(bold_file.path)
            if 'RepetitionTime' not in metadata:
                print(f"Error: Missing RepetitionTime in {bold_file.path}")
                return False
                
        # Check for EEG files with specific extensions
        eeg_extensions = ['edf', 'bdf', 'set', 'fdt']
        eeg_files_found = False
        for ext in eeg_extensions:
            eeg_files = layout.get(suffix='eeg', extension=ext)
            if eeg_files:
                eeg_files_found = True
                break

        if not eeg_files_found:
            print("Error: No EEG files found with the required extensions.")
            return False

        print("Validation completed. No critical issues found.")
        return True

    except Exception as e:
        print(f"Error during validation: {e}")
        return False