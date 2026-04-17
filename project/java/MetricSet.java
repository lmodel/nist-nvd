package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Container for all metric views across CVSS versions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MetricSet  {

  private List<CVSSMetric> cvssV4Metrics;
  private List<CVSSMetric> cvssV3Metrics;
  private List<CVSSMetric> cvssV2Metrics;
  private List<CVSSScoreNote> scoreNotes;

}