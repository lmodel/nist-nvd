package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A CVSS 3.0 score, who gave it, and its subscores.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCvssMetricV30  {

  private String source;
  private String type;
  private CvssV30 cvssData;
  private Float exploitabilityScore;
  private Float impactScore;


}