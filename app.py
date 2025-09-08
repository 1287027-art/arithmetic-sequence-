import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The arithmetic sequence as a list of numbers
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title
    st.title("🔢 Arithmetic Sequence Generator")
    st.write("Generate arithmetic sequences by providing the first term, common difference, and number of terms.")
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=0.1,
            help="The first term of the arithmetic sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=0.1,
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (must be positive)"
        )
    
    # Input validation
    if num_terms <= 0:
        st.error("⚠️ Number of terms must be a positive integer!")
        return
    
    if num_terms > 1000:
        st.warning("⚠️ For performance reasons, please limit the number of terms to 1000 or less.")
        return
    
    # Generate sequence
    try:
        sequence = generate_arithmetic_sequence(first_term, common_difference, int(num_terms))
        
        # Display formula
        st.header("Formula")
        st.latex(f"a_n = {first_term} + (n-1) \\times {common_difference}")
        st.write(f"Where **a₁ = {first_term}**, **d = {common_difference}**, and **n = {int(num_terms)}**")
        
        # Display sequence
        st.header("Generated Sequence")
        
        # Show sequence as a formatted string
        if len(sequence) <= 20:
            # For shorter sequences, display all terms in a single line
            sequence_str = ", ".join([f"{term:g}" for term in sequence])
            st.write(f"**Sequence:** {sequence_str}")
        else:
            # For longer sequences, display in a more compact format
            preview = sequence[:10]
            preview_str = ", ".join([f"{term:g}" for term in preview])
            st.write(f"**First 10 terms:** {preview_str}, ...")
        
        # Display in expandable section for longer sequences
        with st.expander("View All Terms"):
            # Create a formatted display of all terms
            if len(sequence) <= 100:
                # Display as numbered list for sequences up to 100 terms
                for i, term in enumerate(sequence, 1):
                    if i % 10 == 1:  # Start a new line every 10 terms
                        if i > 1:
                            st.write("")  # Add spacing
                        terms_row = []
                    
                    terms_row.append(f"a₍{i}₎ = {term:g}")
                    
                    if i % 10 == 0 or i == len(sequence):  # End of row or last term
                        st.write(" | ".join(terms_row))
            else:
                # For very long sequences, display as a simple list
                terms_per_row = 10
                for i in range(0, len(sequence), terms_per_row):
                    row_terms = sequence[i:i + terms_per_row]
                    row_str = ", ".join([f"{term:g}" for term in row_terms])
                    st.write(f"Terms {i+1}-{min(i+terms_per_row, len(sequence))}: {row_str}")
        
        # Display statistics
        st.header("Sequence Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("First Term", f"{sequence[0]:g}")
        
        with col2:
            st.metric("Last Term", f"{sequence[-1]:g}")
        
        with col3:
            st.metric("Sum of Terms", f"{sum(sequence):g}")
        
        with col4:
            # Calculate sum using arithmetic series formula: n/2 * (first + last)
            arithmetic_sum = (len(sequence) / 2) * (sequence[0] + sequence[-1])
            st.metric("Sum (Formula)", f"{arithmetic_sum:g}")
        
        # Additional information
        with st.expander("Additional Information"):
            st.write("**About Arithmetic Sequences:**")
            st.write("An arithmetic sequence is a sequence of numbers where each term after the first is found by adding a constant (called the common difference) to the previous term.")
            st.write("")
            st.write("**General Formula:** aₙ = a₁ + (n-1)d")
            st.write("- aₙ = nth term")
            st.write("- a₁ = first term") 
            st.write("- d = common difference")
            st.write("- n = term position")
            st.write("")
            st.write("**Sum Formula:** S = n/2 × (first term + last term)")
            
    except Exception as e:
        st.error(f"An error occurred while generating the sequence: {str(e)}")
        st.write("Please check your inputs and try again.")

if __name__ == "__main__":
    main()
