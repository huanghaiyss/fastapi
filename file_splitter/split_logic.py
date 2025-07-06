def split_file_by_keyword(input_path, output_dir, keyword):
    part_num = 1
    buffer = []

    with open(input_path, "r", encoding="utf-8", errors="ignore") as infile:
        for line in infile:
            if keyword in line and buffer:
                # Write current part to file
                part_path = f"{output_dir}/part_{part_num}.txt"
                with open(part_path, "w", encoding="utf-8") as out:
                    out.writelines(buffer)
                buffer = []
                part_num += 1
            buffer.append(line)

        # Write last buffer
        if buffer:
            part_path = f"{output_dir}/part_{part_num}.txt"
            with open(part_path, "w", encoding="utf-8") as out:
                out.writelines(buffer)