/*
A KBase module: man4ish_guptamfmd
*/

module man4ish_guptamfmd {

    typedef structure{
        string workspace_name;
        string fastapath;
        float prb;
        int motif_length;
        string obj_name;
     } find_motifs_params;

     typedef structure {
        string workspace_name;
        string genome_ref;
        string featureSet_ref;
        int promoter_length;
        int motif_min_length;
        int motif_max_length;
        string obj_name;
      } extract_input;

     typedef structure {
        string report_name;
        string report_ref;
     } extract_output_params;

     typedef structure{
        string workspace_name;
        string fasta_path;
     } discover_fasta_input;

     typedef structure{
        string workspace_name;
        string SequenceSetRef;
        string fasta_outpath;
      } BuildSeqIn;

     typedef structure{
        string fasta_outpath;
      } BuildSeqOut; 

     typedef structure{
        string workspace_name;
        string genome_ref;
        string SS_ref;
        int promoter_length;
        int motif_min_length;
        int motif_max_length;
        string obj_name;
        int background;
        int mask_repeats;
        mapping<string, string> background_group;
      } discover_seq_input;

      funcdef find_motifs(find_motifs_params params)
          returns (extract_output_params output) authentication required;

      funcdef DiscoverMotifsFromFasta(discover_fasta_input params)
          returns (extract_output_params output) authentication required;

      funcdef DiscoverMotifsFromSequenceSet(discover_seq_input params)
          returns (extract_output_params output) authentication required;

      funcdef BuildFastaFromSequenceSet(BuildSeqIn params)
        returns (BuildSeqOut output) authentication required;
 

      /*funcdef run_man4ish_guptamfmd(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;*/

};
