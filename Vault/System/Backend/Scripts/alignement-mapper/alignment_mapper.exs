# alignment_mapper.exs
# Parses mock character alignment data and outputs an alignment map

defmodule AlignmentMapper do
  def run do
    characters = [
      %{name: "Ari", logic: 8, emotion: 2},
      %{name: "Ryn", logic: 3, emotion: 7},
      %{name: "Luma", logic: 5, emotion: 5}
    ]

    IO.puts("🧭 Character Alignment Map")
    IO.puts("=========================")

    Enum.each(characters, fn char ->
      type =
        cond do
          char.logic > char.emotion -> "🧠 Logical"
          char.emotion > char.logic -> "💓 Emotional"
          true -> "⚖️ Balanced"
        end

      IO.puts("#{char.name}: #{type} (Logic: #{char.logic}, Emotion: #{char.emotion})")
    end)
  end
end

AlignmentMapper.run()
