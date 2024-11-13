from llm_chains import load_vectordb, create_embeddings

def main():
    try:
        # Load the vector database without token argument if it's not supported
        vector_db = load_vectordb(create_embeddings())

        # Perform a similarity search
        query = "HoVer dataset"
        output = vector_db.similarity_search(query)

        # Print the output
        if output:
            print("Similarity Search Results:")
            for item in output:
                print(item)  # Adjust based on the structure of output
        else:
            print("No results found for the query.")

    except TypeError as te:
        print(f"TypeError occurred: {te}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
