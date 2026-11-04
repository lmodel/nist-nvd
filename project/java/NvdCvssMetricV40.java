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
  A CVSS 4.0 score and who gave it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCvssMetricV40  {

  private String source;
  private String type;
  private CvssV40 cvssData;


}