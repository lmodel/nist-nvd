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
  A CVSS 2.0 score, who gave it, and NVD's figures beside it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCvssMetricV2  {

  private String source;
  private String type;
  private CvssV20 cvssData;
  private Float exploitabilityScore;
  private Float impactScore;
  private String baseSeverity;
  private Boolean acInsufInfo;
  private Boolean obtainAllPrivilege;
  private Boolean obtainUserPrivilege;
  private Boolean obtainOtherPrivilege;
  private Boolean userInteractionRequired;


}