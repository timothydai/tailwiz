import tailwiz
import pandas as pd


def test_parse_no_training_data():
    results = tailwiz.parse(
        pd.DataFrame(
            [['When was the Eiffel Tower constructed?', 'The Eiffel Tower was constructed in 2000']], columns=['prompt', 'context']
        )
    )
    assert len(results) == 1
    assert 'label_from_tailwiz' in results.columns
    assert type(results.label_from_tailwiz.iloc[0]) == str


def test_parse():
    results = tailwiz.parse(
        pd.DataFrame([['When was the Eiffel Tower constructed?', 'The Eiffel Tower was constructed in 2000']], columns=['prompt', 'context']),
        pd.DataFrame([
            ('When were the Pyramids constructed?', 'The Pyramids were constructed in 1930', '1930'),
            ('When was the Earth constructed?', 'The Earth was constructed in 2013', '2013'),
        ], columns=['prompt', 'context', 'label']), False)
    assert len(results) == 1
    assert 'label_from_tailwiz' in results.columns
    assert type(results.label_from_tailwiz.iloc[0]) == str


def test_parse_with_metrics():
    results, metrics = tailwiz.parse(
        pd.DataFrame([['When was the Eiffel Tower constructed?', 'The Eiffel Tower was constructed in 2000']], columns=['prompt', 'context']),
        pd.DataFrame([
            ['When were the Pyramids constructed?', 'The Pyramids were constructed in 1930', '1930'],
            ['When was the Earth constructed?', 'The Earth was constructed in 2013', '2013'],
        ], columns=['prompt', 'context', 'label']), True)
    assert len(results) == 1
    assert 'label_from_tailwiz' in results.columns
    assert type(results.label_from_tailwiz.iloc[0]) == str
    assert metrics is not None
    assert 'rouge1' in metrics
    assert type(metrics['rouge1']) == float