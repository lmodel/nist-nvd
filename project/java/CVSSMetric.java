package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Individual CVSS vector and score attribution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CVSSMetric  {

  private String version;
  private String vectorString;
  private Float baseScore;
  private String baseSeverity;
  private String source;
  private String providerLabel;
  private String scoringJustification;

}